'use-client'
import Layout from "@/app/components/Layout";
import React, { useEffect, useState } from "react"


interface Article {
    id: number;
    title: string;
    content: string;
  }

   
const ArticlePage = ({params}: {params : Promise<{id: string}>}) => {

    const [article, setArticle] = useState<Article | null>(null)

    useEffect(() => {

     const fetchArticle = async () => {
        try {
            const resolvedParams = await params
            const response = await fetch(`http://127.0.0.1:5000/article/${resolvedParams.id}`)
            const data = await response.json()
            setArticle(data)
        } catch (error) {
            console.log('Error al obtener el artículo', error)
        }
     }

     fetchArticle()

    }, [params])

    if(!article) {
        return (
            <Layout>
                <div className="container mx-auto py-10">
                    <p className="text-center">Cargando Artículo......</p>
                </div>
            </Layout>
        )
    }

    return (
        <Layout>
            <div className="container mx-auto py-10">
                <h1 className="text-4xl font-bold mb-6 text-indigo-600">{article.title}</h1>
                <p className="text-gray-700">{article.content}</p>
            </div>
        </Layout>
    )
}

export default ArticlePage
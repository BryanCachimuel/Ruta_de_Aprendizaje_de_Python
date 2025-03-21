'use client'
import Layout from "@/app/components/Layout";
import { useArticle } from "@/context/ArticleProvider";
import { Article } from "@/types/article";
import React, { useState, useEffect } from "react"

   
const ArticlePage = ({params}: {params : Promise<{id: string}>}) => {

    const [article, setArticles] = useState<Article | null>(null);
    const { fetchArticleById } = useArticle()

    useEffect(() => {
        const loadArticle = async() => {
            try {
                const resolvedParams = await params;
                const articleData = await fetchArticleById(parseInt(resolvedParams.id))
                setArticles(articleData)
            } catch (error) {
                console.error('Error al obtener el artículo', error)
            }
        }
        loadArticle();
    }, [params, fetchArticleById])
    

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
'use client'
import { useState, useEffect} from "react";
import Layout from "./components/Layout";
import Card from "./components/Card";

interface Article {
  id: number;
  title: string;
  content: string;
  image_url: string;
  author: string;
  created_at: string;
}

export default function Home() {

  const [articles, setArticles] = useState<Article[]>([])
  console.log(articles)

  useEffect(() => {
    
    fetch('http://localhost:5000/articles')
    .then(response => response.json())
    .then(data => setArticles(data))
    .catch(error => console.log('Error al obtener los artículos: ', error))

  }, [])
  

  return (
    <>
      <Layout>
        <div className="container mx-auto py-10">
          <h1 className="text-4xl font-bold text-center mb-6 text-indigo-600">Últimos Artículos</h1>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
              {
                articles.map((article) => (
                 <Card
                  key={article.id}
                  id={article.id}
                  title={article.title}
                  content={article.content}
                  image_url={article.image_url}
                  author={article.author}
                  created_at={article.created_at}
                 />
                ))
              }
          </div>
        </div>
      </Layout>
    </>
  );
}

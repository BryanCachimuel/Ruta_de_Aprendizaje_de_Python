"use client";
import { useState, useEffect } from "react";
import Layout from "./components/Layout";
import Card from "./components/Card";
import { Article } from "@/types/article";
import { AuthProvider } from "@/context/AuthProvider";

export default function Home() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [filteredArticles, setFilteredArticles] = useState<Article[]>([]);
  console.log(articles);

  useEffect(() => {
    fetch("http://localhost:5000/articles")
      .then((response) => response.json())
      .then((data) => {
        setArticles(data);
        setFilteredArticles(data);
      })
      .catch((error) => console.log("Error al obtener los artículos: ", error));
  }, []);

  /* consumir el endponit de artículo favorito */
  const toggleFavorite = (id: number) => {
    setArticles((prevArticles) =>
      prevArticles.map((article) =>
        article.id === id
          ? {
              ...article,
              isFavorite: !article.isFavorite,
            }
          : article
      )
    );

    const updateArticle = articles.find((article) => article.id === id);

    fetch(`http://localhost:5000/favorite/${id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        isFavorite: updateArticle ? !updateArticle.isFavorite : false,
      }),
    }).catch((error) =>
      console.error("Error al actualizar el artículo favorito", error)
    );
  };

  return (
    <AuthProvider>
      <Layout articles={articles} setFilteredArticles={setFilteredArticles}>
        <div className="container mx-auto py-10">
          <h1 className="text-4xl font-bold text-center mb-6 text-indigo-600">
            Últimos Artículos
          </h1>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {filteredArticles.map((article) => (
              <Card
                key={article.id}
                id={article.id}
                title={article.title}
                content={article.content}
                image_url={article.image_url}
                author={article.author}
                created_at={article.created_at}
                isFavorite={article.isFavorite}
                toggleFavorite={toggleFavorite}
              />
            ))}
          </div>
        </div>
      </Layout>
    </AuthProvider>
  );
}

"use client";
import Layout from "./components/Layout";
import Card from "./components/Card";
import { AuthProvider } from "@/context/AuthProvider";
import { ArticleProvider, useArticle } from "@/context/ArticleProvider";

export default function Home() {
 return(
  <ArticleProvider>
    <AuthProvider>
      <HomeContent/>
    </AuthProvider>
  </ArticleProvider>
 )
}

function HomeContent(){
  const { filteredArticles, loading } = useArticle()

if(loading) return <p>Cargando Artículos...</p>

  return (
      <Layout>
        <div className="container mx-auto py-10">
          <h1 className="text-4xl font-bold text-center mb-6 text-indigo-600">
            Últimos Artículos
          </h1>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {filteredArticles.map((article) => (
              <Card
                key={article.id}
                id={article.id}
              />
            ))}
          </div>
        </div>
      </Layout>

  );
}

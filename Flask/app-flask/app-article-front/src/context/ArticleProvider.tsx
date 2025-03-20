import { Article, ArticleContextType } from "@/types/article";
import React, {createContext, useContext, useState, useEffect} from "react";

const ArticleContext = createContext<ArticleContextType | undefined>(undefined);

export const ArticleProvider: React.FC<{children: React.ReactNode}> = ({children}) => {

    const [articles, setArticles] = useState<Article[]>([])
    const [filteredArticles, setFilteredArticles] = useState<Article[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {

        const fetchArticles = async () => {
            try {
                const response = await fetch('http://localhost:5000/articles');
                const data = await response.json()
                setArticles(data)
                setFilteredArticles(data)
            } catch (error) {
                console.log('Error al obtener los artículos', error)
            } finally {
                setLoading(false)
            }
        }
        
        fetchArticles();

      }, []);

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

        <ArticleContext.Provider value={{articles, filteredArticles, setFilteredArticles, toggleFavorite, loading}}>
            {children}
        </ArticleContext.Provider>

      )

}

export const useArticle = () => {
    const context = useContext(ArticleContext)
    if(!context){
        throw new Error('useArticles debe usarse dentro de un Articleprovider')
    }
    return context;
}


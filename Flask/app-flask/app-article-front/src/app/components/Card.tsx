import React from 'react'
import Link from 'next/link'
import { CardProps } from '@/types/article'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart as fasHeart } from '@fortawesome/free-solid-svg-icons'
import { faHeart as farHeart } from '@fortawesome/free-solid-svg-icons'
import { useAuth } from '@/context/AuthProvider'
import { useArticle } from '@/context/ArticleProvider'

const Card: React.FC<CardProps> = ({id}) => {

  const { isAuthenticated } = useAuth()
  const { articles, toggleFavorite } = useArticle()
  const article = articles.find(article => article.id === id)

  if(!article) return null

  return (
      <div className='bg-gray-100 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300'>
   
        <img src={article.image_url} alt={article.title} className='w-full h-48' />
    
        <div className='p-6'>
         <h2 className='text-2xl font-bold text-indigo-600 mb-2'>{article.title}</h2>
         <p className='text-gray-700'>{article.content.slice(0, 100)}...</p>
         <p className='text-sm font-medium text-gray-900'>Autor del Artículo: {article.author}</p>
         <p className='text-xs text-gray-900'>{article.created_at}</p>
        </div>
        <div className='p-4 bg-indigo-600 text-center'>
            <Link href={`/page/article/${id}`} className='text-white font-semibold hover:text-gray-300 cursor-pointer'>
                <span>Leer Más</span>
            </Link>
        </div>
        <hr />

        <div className='p-4 bg-indigo-600 text-center'>
          {isAuthenticated && (
              <button
                onClick={() =>toggleFavorite(id)}
                className='bg-white/90 backdrop-blur-sm rounded-full p-2.5 shadow-lg hover:bg-white transition-all duration-300'
              >
              <FontAwesomeIcon
                  icon={article.isFavorite ? fasHeart : farHeart}
                  className={`h-5 w-5 ${
                    article.isFavorite ? 'text-red-500' : 'text-gray-600'
                  } group-hover:scale-100 transition-all duration-300`}
              />
              </button>
          )

          }
          
        </div>
      </div>
    )
}

export default Card
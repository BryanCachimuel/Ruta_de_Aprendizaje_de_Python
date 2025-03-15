import React from 'react'
import Link from 'next/link'

interface CardProps {
    id: number;
    title: string;
    content: string;
    image_url: string;
    author: string;
    created_at: string
}

const Card: React.FC<CardProps> = ({id, title, content, image_url,author,created_at}) => {
    return (
      <div className='bg-gray-100 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300'>
        {
          image_url && (
            <img src={image_url} alt={title} className='w-full h-48' />
          )
        }
        <div className='p-6'>
         <h2 className='text-2xl font-bold text-indigo-600 mb-2'>title</h2>
         <p className='text-gray-700'>{content.slice(0, 100)}...</p>
         <p className='text-sm font-medium text-gray-900'>Autor del Artículo: {author}</p>
         <p className='text-xs text-gray-900'>{created_at}</p>
        </div>
        <div className='p-4 bg-indigo-600 text-center'>
            <Link href={`/page/article/${id}`} className='text-white font-semibold hover:text-gray-300 cursor-pointer'>
                <span>Leer Más</span>
            </Link>
        </div>
      </div>
    )
}

export default Card
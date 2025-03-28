import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlusCircle, faSignInAlt } from '@fortawesome/free-solid-svg-icons'
import SearchBar from './SearchBar';
import { Article } from '@/types/article';


interface NavbarProps {
  articles: Article[];
  setFilteredArticles?: (articles: Article[]) => void;
  onOpenCreateModal: () => void;
}


const Navbar: React.FC<NavbarProps> = ({articles, setFilteredArticles, onOpenCreateModal}) => {

  const [isAuthenticated, setIsAuthenticated] = useState(false)

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await fetch('http://localhost:5000/check-auth', {
          method: 'GET',
          credentials: 'include'
        })
        const data = await response.json()
        setIsAuthenticated(data.authenticated)
      } catch (error) {
        console.log('Error al verificar la autenticación', error)
      }
    }
    checkAuth()
  }, [])

  const handleLogout = async () => {
    try {
      await fetch('http://localhost:5000/logout',{
        method: 'POST',
        credentials: 'include',
      })
      setIsAuthenticated(false)
    } catch (error) {
      console.log('Error al cerrar sesión', error)
    }
  }
  

  return (
    <nav className='bg-indigo-600 text-white p-4'>
       <div className="container mx-auto flex justify-between items-center">
        <a href="/" className='text-xl font-bold'>Mi Artículo</a>

            {/* Componente para Buscar */}
          <SearchBar
              articles={articles}
              setFilteredArticles={setFilteredArticles}
          />

            <ul className='flex space-x-6 items-center'>

            {
              isAuthenticated && (
                <li>
                <button onClick={onOpenCreateModal} className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faPlusCircle} className='mr-2 h-6 w-6'/>
                   Crear Artículo
                </button>
              </li>
              )
            }

             {!isAuthenticated ? (
              <li>
                <Link href="/page/login" className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faSignInAlt} className='mr-2 h-6 w-6'/>
                   Iniciar Sesión
                </Link>
              </li>
             )  :  (
              <li>
                <button 
                  onClick={handleLogout}
                  className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faSignInAlt} className='mr-2 h-6 w-6'/>
                   Cerrar Sesión
                </button>
              </li>
             )}
            </ul>

       </div>
    </nav>
  )
}

export default Navbar

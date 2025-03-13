import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch, faPlusCircle, faSignInAlt } from '@fortawesome/free-solid-svg-icons'

const Navbar = () => {

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
  

  return (
    <nav className='bg-indigo-600 text-white p-4'>
       <div className="container mx-auto flex justify-between items-center">
        <a href="/" className='text-xl font-bold'>Mi Artículo</a>

        <div className='flex-grow'>
          <div className="relative max-w-md mx-auto">
                  <FontAwesomeIcon icon={faSearch} className='text-white absolute left-3 top-3 h-5 w-5'/>
                      <input 
                      type="text" 
                      placeholder="Buscar artículos..."
                      className="bg-gray-300 text-black rounded-full pl-10 pr-4 py-2 w-full focus:outline-none"
                      />  
              </div>
        </div>

            <ul className='flex space-x-6 items-center'>

            {
              isAuthenticated && (
                <li>
                <Link href="/create" className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faPlusCircle} className='mr-2 h-6 w-6'/>
                   Crear Artículo
                </Link>
              </li>
              )
            }

             

              <li>
                <Link href="/page/login" className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faSignInAlt} className='mr-2 h-6 w-6'/>
                   Iniciar Sesión
                </Link>
              </li>

            </ul>

       </div>
    </nav>
  )
}

export default Navbar

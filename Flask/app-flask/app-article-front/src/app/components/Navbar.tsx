import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch, faPlusCircle, faSignInAlt } from '@fortawesome/free-solid-svg-icons'

const Navbar = () => {
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
              <li>
                <a href="/create" className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faPlusCircle} className='mr-2 h-6 w-6'/>
                   Crear Artículo
                </a>
              </li>

              <li>
                <a href="/login" className='flex items-center hover:text-gray-300'>
                   <FontAwesomeIcon icon={faSignInAlt} className='mr-2 h-6 w-6'/>
                   Iniciar Sesión
                </a>
              </li>

            </ul>

       </div>
    </nav>
  )
}

export default Navbar

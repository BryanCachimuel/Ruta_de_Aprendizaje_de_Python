import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'

const Navbar = () => {
  return (
    <nav className='bg-indigo-600 text-white p-4'>
       <div className="container mx-auto flex justify-between items-center">
            <div className="flex items-center space-x-4">
                <a href="/" className='text-xl font-bold'>Mi Artículo</a>
                <div className="relative">
                    <input 
                    type="text" 
                    placeholder="Buscar artículos..."
                    className="bg-gray-300 text-black rounded-full pl-10 pr-4 py-2 focus:outline-none"
                    />
                    <FontAwesomeIcon icon={faSearch} className='text-white absolute left-3 top-3 h-5 w-5'/>
                </div>
            </div>
       </div>
    </nav>
  )
}

export default Navbar

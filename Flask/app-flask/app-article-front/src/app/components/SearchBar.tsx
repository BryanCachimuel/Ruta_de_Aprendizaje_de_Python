import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'

const SearchBar = () => {
  return (
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
  )
}

export default SearchBar
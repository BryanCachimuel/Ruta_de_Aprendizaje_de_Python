import React from 'react'

const Navbar = () => {
  return (
    <nav className='bg-indigo-600 text-white p-4'>
        <div className='container mx-auto flex justify-between items-center'>
            <h1 className='text-xl font-bold'>Mi Artículo</h1>
            <ul className='flex space-x-4'>
                <li>
                    <a href="/">Inicio</a>
                </li>
                <li>
                    <a href="/">Crear</a>
                </li>
            </ul>
        </div>
    </nav>
  )
}

export default Navbar

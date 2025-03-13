import React, { useState } from 'react'
import { useRouter } from 'next/router'

const login = () =>{

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')
    const router = useRouter()

    const handleSubmit = async (e:React.FormEvent) => {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email, password})
        })

        if(response.ok){
            router.push('/')
        }
        else{
            const data = await response.json()
            setError(data.error || 'Error al iniciar la sesión')
        }
    }

    return (
      <div className='container mx-auto py-10'>
        <h1 className="text-3xl font-bold text-center mb-6">Iniciar Sesión</h1>
       {error && <p className='text-red-500 text-center mb-4f'>{error}</p>}

       <form onSubmit={handleSubmit} className='max-w-md mx-auto'>
            <div className="mb-4">
                <label className="block text-gray-700">Email</label>
                <input 
                type="email" 
                className="w-full p-2 border border-gray-300 rounded"  
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                />
            </div>
            <div className="mb-4">
                <label className="block text-gray-700">Password</label>
                <input 
                type="password" 
                className="w-full p-2 border border-gray-300 rounded"  
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                />
            </div>
            <button 
            type='submit' 
            className='w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-500'
            >
                Iniciar Sesión
            </button>
       </form>
      </div>
    )

}

export default login
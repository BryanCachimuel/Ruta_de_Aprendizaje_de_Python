import { AuthContextType } from "@/types/auth";
import React, {createContext, useContext, useState, useEffect} from "react";

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{children: React.ReactNode}> = ({children}) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      const checkAuthStatus = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/check-auth', {
                credentials: 'include'
            })
            const data = await response.json()
            setIsAuthenticated(data.authenticated)
        } catch (error) {
            console.error('Error al verificar la autenticación', error)
            setIsAuthenticated(false)
        }  finally {
            setLoading(false)
        }
      }
    }, [])
    
}
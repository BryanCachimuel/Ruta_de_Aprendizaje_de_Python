import React from "react"
import Navbar from "./Navbar"
import Footer from "./Footer"
import { useArticle } from "@/context/ArticleProvider";


interface LayoutProps {
    children: React.ReactNode;
    onOpenCreateModal: () => void;
}


const Layout: React.FC<LayoutProps> = ({children, onOpenCreateModal}) => {

    const { articles, setFilteredArticles } = useArticle()

    return(
        <div className="flex flex-col min-h-screen">
            <Navbar articles={articles} setFilteredArticles={setFilteredArticles} onOpenCreateModal={onOpenCreateModal}/>
            <main className="flex-grow">
                {children}
            </main>
            <Footer/>
        </div>
    )
}

export default Layout
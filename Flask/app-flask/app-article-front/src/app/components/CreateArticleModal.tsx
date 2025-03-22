import { Article } from '@/types/article';
import React from 'react'

interface CreateArticleModalProps {
    onClose: () => void;
    onSubmit: (newArticle: Partial<Article>) => Promise<{success: boolean, message: string}>
}

export const CreateArticleModal: React.FC<CreateArticleModalProps> = ({onClose, onSubmit}) => {
  return (
    <div>CreateArticleModal</div>
  )
}

from document.models import *
from document.serializers import *

class DocumentService:
    def __init__(self):
        pass
    
    @classmethod
    def create_document(cls, title, content, published):
        """
        Creates a new document with the given title, content, and published status.
        
        Args:
            title (str): The title of the new document.
            content (str): The content of the new document.
            published (bool): Whether the new document should be published or not.
            
        Returns:
            dict: A dictionary containing a message indicating whether the document was created successfully or not.
        """
        try:
            document = Document(title=title, content=content, published=published)
            document.save()            
            return {"message": "Document created successfully."}
        except Exception as e:
            return {"message": "Error creating document: " + str(e)}

    @classmethod
    def get_document(cls, id):
        """
        Retrieves the document with the given ID.
        
        Args:
            id (int): The ID of the document to retrieve.
            
        Returns:
            dict: A dictionary containing a message indicating whether the document was retrieved successfully or not, and the retrieved document object.
        """
        try:
            document = Document.objects.get(id=id)
            return {"message": "Document retrieved successfully.", "document": DocumentSerializer(document).data}
        except Exception as e:
            return {"message": "Error retrieving document: " + str(e)}
        
    @classmethod
    def get_all_documents(cls):
        """
        Retrieves all documents.
        
        Returns:
            dict: A dictionary containing a message indicating whether the documents were retrieved successfully or not, and a list of all retrieved document objects.
        """
        try:
            documents = Document.objects.all()
            return {"message": "Documents retrieved successfully.", "documents": DocumentSerializer(documents, many=True).data}
        except Exception as e:
            return {"message": "Error retrieving documents: " + str(e)}
        
    @classmethod
    def update_document(cls, id, title, content, published):
        """
        Updates the document with the given ID with the new title, content, and published status.
        
        Args:
            id (int): The ID of the document to update.
            title (str): The new title of the document.
            content (str): The new content of the document.
            published (bool): The new published status of the document.
            
        Returns:
            dict: A dictionary containing a message indicating whether the document was updated successfully or not.
        """
        try:
            document = Document.objects.get(id=id)
            document.title = title
            document.content = content
            document.published = published
            document.save()
            return {"message": "Document updated successfully."}
        except Exception as e:
            return {"message": "Error updating document: " + str(e)}

    @classmethod
    def delete_document(cls, id):
        """
        Deletes the document with the given ID.
        
        Args:
            id (int): The ID of the document to delete.
            
        Returns:
            dict: A dictionary containing a message indicating whether the document was deleted successfully or not.
        """
        try:
            document = Document.objects.get(id=id)
            document.delete()
            return {"message": "Document deleted successfully."}
        except Exception as e:
            return {"message": "Error deleting document: " + str(e)}
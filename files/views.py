from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import RetrieveDestroyAPIView

from .models import File
from .serializers import FileSerializer
# Create your views here.

class files(APIView):
    serializer_class = FileSerializer    
    permission_classes = (IsAuthenticatedOrReadOnly,)    
    
    def get(self,request,format = None):
        files = File.objects.all()
        ret = {'files':[]}

        for file in files:
            ret_file={}
            ret_file['url'] = 'http://{0}/user-uploads/{1}'.format(request.get_host(), str(file.file))
            ret_file['owner'] = str(file.owner)
            ret_file['id'] = str(file.id)             
            ret['files'].append(ret_file)             
        
        if not ret['files'] : #Empty lists return false
            ret['detail'] = "No Files available"
            
        return Response(ret, status=status.HTTP_200_OK)
        
    def post(self,request,format = None):
        serializer = FileSerializer(data = request.data)
            
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
     
class file(RetrieveDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer    
    permission_classes = (IsAuthenticatedOrReadOnly,)  
      
    def retrieve(self, request, *args, **kwargs):
        file = self.get_object()  
        
        ret_file={}
        ret_file['url'] = 'http://{0}/user-uploads/{1}'.format(request.get_host(), str(file.file))
        print(file.file.__dict__)
        ret_file['owner'] = str(file.owner)
        ret_file['id'] = str(file.id)         
    
        return Response(ret_file, status=status.HTTP_200_OK)
    
         

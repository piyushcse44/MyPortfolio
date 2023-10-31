from rest_framework import serializers


class ServicesSerializer(serializers.Serializer):
  
    Name = serializers.CharField(max_length=200)
    Price = serializers.CharField(max_length=200)
    logo = serializers.CharField(max_length=200)
    Description = serializers.CharField()
    DiscoveryMore = serializers.URLField(max_length=200)


class ContactFormSerailizer(serializers.Serializer):

    FirstName = serializers.CharField(max_length=200)
    LastName =serializers.CharField(max_length=200)
    Email = serializers.EmailField(max_length=200) 
    Services = ServicesSerializer(many = True)
    Description = serializers.CharField()






    
    
import graphene

from graphene import relay, ObjectType

from graphene_django.types import DjangoObjectType

from graphene_django.filter import DjangoFilterConnectionField

from myapp.models import Model1A

from django.shortcuts import get_object_or_404


class Model1ANode(DjangoObjectType):
    class Meta:
        model=Model1A
        filter_fields = ["id", "field1A"]
        interfaces=(relay.Node, )


class Model1AConnection(relay.Connection):
    class Meta:
        node = Model1ANode


class Query:
    # model1a = relay.ConnectionField(Model1AConnection)

    # def resolve_model1a(self, info, **kwargs):
    #     return Model1A.objects.all()

    model1a = relay.Node.Field(Model1ANode)
    all_model1a = DjangoFilterConnectionField(Model1ANode)

#################################################################

class Model1ACreateInput(graphene.InputObjectType):
    field1A = graphene.String(required=True)

class CreateModel1A(relay.ClientIDMutation):
    
    class Input:
        field1A = graphene.String(required=True)

    model1a = graphene.Field(Model1ANode)

    def mutate_and_get_payload(root, info, **input):
        model1a = Model1A(
            field1A=input.get('field1A'),
        )
        model1a.save()    
        return CreateModel1A(model1a=model1a)

##############################

    # class Input:
    #     field1A = graphene.Field(Model1ACreateInput)

    # model1a = graphene.Field(Model1ANode)

    # def mutate_and_get_payload(root, info, **input):
    #     model1a = Model1A.objects.create(**input.get('field1A'))
    #     return CreateModel1A(model1a=model1a)

########################################

class Mutation(graphene.AbstractType):
    create_model1a = CreateModel1A.Field()

###

""" # # # model1a = relay.Node.Field(Model1ANode)
# query {model1a(id:"TW9kZWwxQU5vZGU6MQ=="){
#   field1A
#   id
# }}
 """

###

""" 
query{
  allModel1a{
    edges{
      node{
        id 
        field1A
      }
    }
  }
  
}
 """

###

""" 
# query{
#   allModel1a{
#     edges{
#       node{
#         id 
#         field1A
#       }
#     }
#   }
  
# } """

###

""" 
# # field1A = graphene.String(required=True)
mutation{
  createModel1a(
    input:{
      field1A:"dew3243e"
    }
  ){
    model1a{
      field1A
    }
  }
}
 """
###

""" 
# # field1A = graphene.Field(Model1ACreateInput)
# mutation{
#   createModel1a(
#     input:{
#       field1A:{
#         field1A:"dene23324"
#       }
#     }
#   ){
#     model1a{
#       id
#       field1A
#     }
#   }
# }
 """


from comunidadedash import app, database
from comunidadedash.models import Usuario, Post

#with app.app_context():
    #database.create_all()

#with app.app_context():
    #usuario = Usuario(username="lucas", email="Lucas.vgz38@gmail.com", senha="123456")
    #usuario2 = Usuario(username="grasi", email="grasi@gmail.com", senha="123456")
    #database.session.add(usuario)
    #database.session.add(usuario2)
    #database.session.commit()

#with app.app_context():
    #meus_usuarios = Usuario.query.all()
    #print(meus_usuarios)
    #primeiro_usuario = Usuario.query.first()
    #print(primeiro_usuario.senha)
#deletar tabela
#
with app.app_context():
    database.drop_all()
    database.create_all()


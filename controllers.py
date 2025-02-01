from sqlalchemy import create_engine
from settings.db import session
from sqlalchemy.exc import NoResultFound
from models import Pessoa
import hashlib


def encriptar_senha(senha):
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    return hash_senha

class PessoaController():
    
    erros = ''
    
    @classmethod
    def validar_nome(cls,nome):
        
        tamanho = len(nome)
        
        if tamanho < 3:
            cls.erros += 'Nome muito curto, favor inserir um maior.\n'
            return False
        
        if tamanho > 100:
            cls.erros += 'Nome muito grande, favor inserir um menor.\n'
            return False
        
        return True
        
    
    @classmethod
    def validar_email(cls, email):
        if len(email) > 100:
            cls.erros += 'E-mail muito grande, favor inserir um menor.\n'
            return False
        
        usuarios = session.query(Pessoa).filter(Pessoa.email == email).all()
        
        if len(usuarios) > 0:
            cls.erros += 'Este e-mail já está sendo utilizado por um usuário, favor substituir.\n'
            return False
        
        return True
        
    
    @classmethod
    def validar_senha(cls, senha):
        tamanho = len(senha)
        
        if tamanho < 6:
            cls.erros += 'Senha muito curta, favor inserir uma maior.\n'
            return False
        
        if tamanho > 100:
            cls.erros += 'Senha muito grande, favor inserir uma menor.\n'
            return False
        
        return True
    
    
    @classmethod
    def validar_dados(cls, nome, email, senha):
        
        nome_valido = cls.validar_nome(nome)
        email_valido = cls.validar_email(email)
        senha_valida = cls.validar_senha(senha)
        
        if nome_valido and email_valido and senha_valida:
            return True
        
        return False
    
    
    @classmethod
    def cadastrar(cls, nome, email, senha):
        
        dados_validos = cls.validar_dados(nome, email, senha)
        
        try:
            if dados_validos:
                senha_encriptada = encriptar_senha(senha)
                print(senha_encriptada)
                
                p = Pessoa(nome=nome, email=email, senha=senha_encriptada)
                
                session.add(p)
                session.commit()
                print('Cadastro realizado com sucesso!')
            else:
                print('\n\nCadastro não realizado. Corrija os problemas seguintes e tente novamente:\n')
                print(cls.erros)
        
        except Exception as e:
            return print(f'Problema ao tentar salvar usuário: {e}')


class LoginController():
    @classmethod
    def login(cls, email, senha):
        senha_encriptada = encriptar_senha(senha)
        
        try:
            usuario = session.query(Pessoa).filter_by(email = email, senha = senha_encriptada).one()
            
            if usuario:
                return print(f'Login realizado com sucesso, {usuario.nome}!')
        except NoResultFound:
            return print('Problema ao tentar logar. Verifique as informações de login.')
        except Exception as e:
            return print(f'Problema ao tentar logar: {e}')


# PessoaController.cadastrar('Antônio', 'antonio@email.com', '123456')
# LoginController.login('antonio@email.com', '123456')
import argparse
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService

class CLIController:
    def __init__(self, poll_service: PollService, user_service: UserService, nft_service: NFTService):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.parser = argparse.ArgumentParser(description='Sistema de Encuestas CLI')
        subparsers = self.parser.add_subparsers(dest='command')
        subparsers.add_parser('listar_encuestas')
        crear = subparsers.add_parser('crear_encuesta')
        crear.add_argument('--id')
        crear.add_argument('--pregunta')
        crear.add_argument('--opciones', nargs='+')
        crear.add_argument('--duracion', type=int)
        cerrar = subparsers.add_parser('cerrar_encuesta')
        cerrar.add_argument('--id')
        ver = subparsers.add_parser('ver_resultados')
        ver.add_argument('--id')

    def run(self, args=None):
        args = self.parser.parse_args(args)
        if args.command == 'listar_encuestas':
            encuestas = self.poll_service.encuesta_repo.get_polls_json()
            print(encuestas)
        elif args.command == 'crear_encuesta':
            poll = self.poll_service.create_poll(args.id, args.pregunta, args.opciones, args.duracion)
            print('Encuesta creada:', poll.__dict__)
        elif args.command == 'cerrar_encuesta':
            self.poll_service.close_poll(args.id)
            print('Encuesta cerrada')
        elif args.command == 'ver_resultados':
            res = self.poll_service.get_results(args.id)
            print('Resultados:', res)

from spyne import Iterable, Integer, Unicode, rpc, Application, Service
from spyne.protocol.soap import Soap11


class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name


def create_app():
    application = Application(
        [HelloWorldService], 'spyne.examples.flask',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )

    return application


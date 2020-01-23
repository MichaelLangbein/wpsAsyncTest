from pywps import Process, LiteralInput, LiteralOutput, ComplexOutput, ComplexInput, Format
from pywps.app.Common import Metadata
from pywps.validator.mode import MODE
from pywps.inout.formats import FORMATS


def sayHi(name):
    return f"Hello there, {name}!"


def _handler(request, response):
        name = request.inputs['name'][0].data
        output = sayHi(name)
        response.outputs['greeting'].data = output
        return response


class SayHiWps(Process):
    def __init__(self):

        inputs = [
            LiteralInput('name', data_type='string')
        ]
        outputs = [
            LiteralOutput('greeting', 'greeting', data_type='string')
        ]

        super(SayHiWps, self).__init__(
            _handler,
            identifier='SayHi',
            version='1.0.0',
            title='SayHi',
            abstract='Says hi.',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )


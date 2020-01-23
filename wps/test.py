import requests


url = "http://localhost:1410/wps?service=WPS&request=Execute&version=1.0.0&identifier=SayHi"

body = """
<wps:Execute xmlns:wps="http://www.opengis.net/wps/1.0.0" service="WPS" version="1.0.0">
   <p0:Identifier xmlns:p0="http://www.opengis.net/ows/1.1">SayHi</p0:Identifier>
   <wps:DataInputs>
      <wps:Input>
        <p0:Identifier xmlns:p0="http://www.opengis.net/ows/1.1">name</p0:Identifier>
        <p0:Title xmlns:p0="http://www.opengis.net/ows/1.1">name</p0:Title>
        <p0:Abstract xmlns:p0="http://www.opengis.net/ows/1.1"></p0:Abstract>
        <wps:Data>
            <wps:LiteralData>Michael</wps:LiteralData>
        </wps:Data>
    </wps:Input>
   </wps:DataInputs>
   <wps:ResponseForm>
      <wps:ResponseDocument storeExecuteResponse="true" status="true">
         <wps:Output mimeType="application/text" asReference="false">
            <p0:Identifier xmlns:p0="http://www.opengis.net/ows/1.1">greeting</p0:Identifier>
         </wps:Output>
      </wps:ResponseDocument>
   </wps:ResponseForm>
</wps:Execute>
"""

r = requests.post(url = url, data = body) 
# V1beta1HTTPIngressRuleValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The network address to listen HTTP(s) connections on. | [optional] 
**alpn** | **list[str]** | Application-Layer Protocol Negotiation (ALPN) is a Transport Layer Security (TLS) extension for application layer protocol negotiation. ALPN allows the application layer to negotiate which protocol should be performed over a secure connection in a manner which avoids additional round trips and which is independent of the application layer protocols. It is used by HTTP/2. If provided a list of alpn will be added to port as alpn option1,option2,... If SecretName is Provided this secret will be used to terminate SSL with alpn options. If Secret name is not provided backend server is responsible for handling SSL. | [optional] 
**no_tls** | **bool** | Set noTLS &#x3D; true to force plain text. Else, auto detect like present | [optional] 
**node_port** | **str** | Specifies the node port of the referenced service. | [optional] 
**paths** | [**list[V1beta1HTTPIngressPath]**](V1beta1HTTPIngressPath.md) | A collection of paths that map requests to backends. | 
**port** | **str** | port to listen http(s) connections. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



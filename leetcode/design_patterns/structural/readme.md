# Other Structural Patterns not discussed

## Proxy

    Proxy becomes handy when creating a highly resource-intensive object. The problem we need to solve here is postponing our object creation as long as possible, due to the high-resource requirement of the object we're creating. Therefore, there's a need for a placeholder that will, in turn, create the object when its creation is absolutely necessary. Here's our scenario. We create an instance of a producer class only when it's available because only a fixed number of producer objects can exist at a given time. Our proxy is an artist who is checking to see if the producer becomes available for a guest. In the proxy design pattern, clients interact with a proxy object most of the time until the resource-intensive object becomes available. The proxy object is in charge of creating the resource-intensive objects. Adapter and Decorator are related to the proxy design pattern.

## Bridge

    - The bridge pattern helps untangle an unnecessarily complicated class hierarchy. Especially when implementation-specific classes are mixed with implementation-independent classes. The problem here is that there are two parallel or orthogonal abstractions. One is implementation specific, and the other is implementation independent. Our scenario involves implementation-independent circle abstraction and implementation-dependent circle abstraction. The implementation-dependent circle abstraction involves how to draw a circle. And the implementation-independent circle abstraction involves defining the properties of a circle and scaling it. Our solution is avoiding abstracting both implementation-specific and implementation-independent classes in a single class hierarchy. The abstract factory and adapter patterns are the related patterns to the bridge design pattern.
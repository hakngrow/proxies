# Find Me Proxies (FIMP)
Proxies are intermediaries.  We need them for a variety of reasons, to filter web content, to go around 
restrictions such as internet blocks, to screen downloads and uploads and mostly to provide anonymity 
when surfing the internet.  More on [Wikipedia](https://en.m.wikipedia.org/wiki/Proxy_server) about 
proxies.

FIMP is a simple python script to scrape open and FREE proxy servers from https://free-proxy-list.net/.
Because these are free proxies, there is no guarantee of service availability. So after extracting 
the list of proxy IP addresses, the script can test these proxies by using them to connect to 
https://httpbin.org/ip. httpbin is a HTTP request and response service. It returns the original IP 
address of a HTTP request.  And if we connect to httpbin using the proxy and receives the proxy's 
ip address as a response, we can verify that the proxy is working.

<%
    Integer count = (Integer) application.getAttribute("count");
    if(count == null){
        count = 0;
    }
    count++;
    application.setAttribute("count", count);


%>
<html>
    <head>
        <title>Application Visitor Count</title>
    </head>
    <body>
        <h2>Application Visitor Count</h2>
        Vistor Count: <%= count %>
    </body>
</html>
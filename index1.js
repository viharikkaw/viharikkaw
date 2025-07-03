<html>
    <body>
        <p id="demo">hai</p>
        <p id="demo1">hello</p>
    <button onclick="changeText()">Click</button>    
        <script>
            function changeText() {
                document.getElementById("demo").innerHTML="hello";
                document.getElementById("demo1").innerHTML="welcome to MRECW";
            }
        </script>
    </body>
</html>
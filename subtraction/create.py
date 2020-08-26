#for i in range(0,22):
#    print('<a id="l'+str((i+1))+'" onclick="tablefun('+str(i+1)+',3,'+str((i*5))+','+str(((i+1)*5))+',0)" class="dropdown-item l_s" href="#">3*['+str((i*5))+'...'+str(((i+1)*5))+']</a>')
#print('<a id="l'+str(i)+'" class="btn l_s" href="funtable/l'+str(i)+'.html">'+str(i)+"*[1...99]</a>")
b = '''
<!--Copyright 2020-2021 SUNIL KUMAR YADAV. (https://sunilkuyadav.github.io/MathFun/)-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="titlel"></title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="../cal.css">
    <script src="subtraction.js"></script>
    <script defer src="cdown.js"></script>
</head>

<body>
    <div class="cantainer">
        <div class="main">
            <div class="operation">
                <nav class="navbar navbar-expand-md bg-dark navbar-dark">
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="collapsibleNavbar">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link sp" href="../addition.html">Addition</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../substraction.html">Substraction</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../multiplication.html">Multiplication</a>
                      </li> 
                      <li class="nav-item">
                        <a class="nav-link sp" href="../division.html">Division</a>
                      </li>
                        <li class="nav-item">
                        <a class="nav-link sp" href="../tablefun.html">TableFun</a>
                      </li>
                    </ul>
                  </div>  
                </nav>
            </div>            
            <div class="sub">
            <div class="dropdown">
                <button type="button" class="btn dropdown-toggle btnl" data-toggle="dropdown">Level 1
    </button>
                <div id="qs" class="qs"></div>
                    <div class="text-center dropdown-menu">
                        <a id="l1" onclick="sub(1,10,50,0,0)" class="dropdown-item l_s" href="s1.html">Level 1</a>
                        <a id="l2" onclick="sub(2,100,200,0,0)" class="dropdown-item l_s" href="s2.html">Level 2</a>
                        <a id="l3" onclick="sub(3,200,300,0,0)" class="dropdown-item l_s" href="s3.html">Level 3</a>
                        <a id="l4" onclick="sub(4,300,400,0,0)" class="dropdown-item l_s" href="s4.html">Level 4</a>
                        <a id="l5" onclick="sub(5,500,600,0,0)" class="dropdown-item l_s" href="s5.html">Level 5</a>
                        <a id="l6" onclick="sub(6,600,700,0,0)" class="dropdown-item l_s" href="s6.html">Level 6</a>
                        <a id="l7" onclick="sub(7,700,800,0,0)" class="dropdown-item l_s" href="s7.html">Level 7</a>
                        <a id="l8" onclick="sub(8,900,1000,0,0)" class="dropdown-item l_s" href="s8.html">Level 8</a>
                        <a id="l9" onclick="sub(9,1000,2000,0,0)" class="dropdown-item l_s" href="s9.html">Level 9</a>
                        <a id="l10" onclick="sub(10,2000,3000,0)" class="dropdown-item l_s" href="s10.html">Level 10</a>
                        <a id="l11" onclick="sub(11,3000,4000,0,0)" class="dropdown-item l_s" href="s11.html">Level 11</a>
                        <a id="l12" onclick="sub(12,4000,5000,0,0)" class="dropdown-item l_s" href="s12.html">Level 12</a>
                        <a id="l13" onclick="sub(13,5000,10000,0,0)" class="dropdown-item l_s" href="s13.html">Level 13</a>
                        <a id="l14" onclick="sub(14,10000,15000,0,0)" class="dropdown-item l_s" href="s14.html">Level 14</a>
                        <a id="l15" onclick="sub(14,15000,20000,0,0)" class="dropdown-item l_s" href="s15.html">Level 15</a>
                        <a id="l16" onclick="sub(15,20000,30000,0,0)" class="dropdown-item l_s" href="s16.html">Level 16</a>
                        <a id="l17" onclick="sub(16,30000,70000,0,0)" class="dropdown-item l_s" href="s17.html">Level 17</a>
                        <a id="l18" onclick="sub(18,50000,90000,0,0)" class="dropdown-item l_s" href="s18.html">Level 18</a>
                      
                        
                    </div>
                </div>
                <div id="quest">
                    <div class="question" id="question">start</div>
                    <div id="cd"><div id="app"></div></div>
                </div>
                <hr>
                <div class="input">
                    <div id="option-buttons" class="btn-grid">
                        <button id="btns1" class="btn btnc" href="#">1</button>
                        <button id="btns2" class="btn btnc" href="#">2</button>
                        <button id="btns3" class="btn btnc" href="#">3</button>
                        <button id="btns4" class="btn btnc" href="#">4</button>
                    </div>
                </div>
                <hr>
                <div class="hint">
                    <button id="hintshow" class="hintshow btn" type="button">HINT</button>
                    <h1 id="hints">Substraction</h1>
                </div>
            </div>
        </div>
    </div>
    <footer>
            <div class="cpd">SUNIL KUMAR YADAV &copy; 2020-21</div>
    </footer>
</body>
        <script>
            $( document ).ready(function() {
        $('#l|').click();
    });
        $('.l_s').on('click',function(){
            $('.btnl').text(($(this).text()));
            $('#titlel').text(($(this).text())+" | Substraction");
        });
    </script>
</html>


'''
for i in range(1,19):
    x = b.replace('|',str(i))
    p = ('s'+str(i)+'.html')
    f = open(p,"w")
    f.write(x)
    f.close()
    

        $(document).ready(function(){
            <!--设置下拉菜单-->
            $(".dropdown-menu li a").click(function(){
                var e = document.getElementById("category");
                console.log(e.innerText);
                e.innerText = $(this).text();
            });
            $('#FileUpload').click(function() {
                var form_data = new FormData();
                var file_info =$('#exampleInputFile')[0].files[0];
                var upload_user = $('#uploadUuser').val();
                var category = $('#category').text();
                console.log(file_info);
                console.log(upload_user);
                console.log(category);
                if(category == "请选择文章类别")
                    category = "未知";
                if(upload_user === "")
                    upload_user = "未知"
                var filesize = file_info.size;
                console.log(filesize);
                form_data.append("file",file_info);
                form_data.append("size",filesize);
                form_data.append("upload_user",upload_user);
                form_data.append("category",category);
                if(file_info === undefined){
                    alert('你没有选择任何文件');
                    return false;
                 }
                $.ajax({
                    url:'/summary/upload/',
                    type:'POST',
                    data: form_data,
                    processData: false,  // tell jquery not to process the data
                    contentType: false, // tell jquery not to set contentType
                    success: function(data) {
                        if(data == "fileExist")
                            alert("文件已存在！");
                        else if(data == "uploadsuccess"){
                            alert("文件上传成功！");
                            window.location.href("/summary/index/");
                        }
                        else if(data == "fail"){
                            alert("内部错误，文件上传失败500");
                        }
                    },
                    error:function(result){
                        action();
                        console.log(result);
                        alert("内部错误，文件上传失败");
                    }
                });
            });
        });
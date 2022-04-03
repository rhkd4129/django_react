import React, {useEffect, useState} from "react";
import Axios from "axios";
import Post from "post";
const apiUrl = "http://localhost:8000/api/posts/";

function PostList(){
const [postList,setPostList] = useState([]);
    useEffect(() => {
        Axios.get(apiUrl)
            .then(response=>{
                const {data}  = response;
                console.log("loaded response",response);
                setPostList(data)
            })
            .catch(error => {})
        console.log("mounted");
    }, []);
    return(
        <div>
            <h2>PostList</h2>
            {postList.map(post  =>(
                <Post post={post} key={post.id}/>// 
            ))}
        </div>
    );
}
export default PostList

// axios를 통해 요청을 서버에게 보내면, 서버에서 처리를하고 다시 데이터를 클라이언트에 응답 하게 된다.
// 이를 .then으로 함수인자로(response)로 받아 객체에 담진 데이터가 바로 응답 데이터이다.
// 출처: https://inpa.tistory.com/entry/AXIOS-📚-설치-사용 [👨‍💻 Dev Scroll]
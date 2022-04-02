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
    // {JSON.stringify(post)}
    return(
        <div>
            PostList
            {postList.map(post  =>(
                <Post post={post} key={post.id}/>// 
            ))}
        </div>
    );
}

export default PostList
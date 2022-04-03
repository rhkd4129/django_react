import React from "react";

function Post( {post}){
    const { caption,photo} = post;
    return( 
        <div >
            <img src ={photo} alt = {caption}/>
            {caption} 
        </div>
        );
}

export default Post;
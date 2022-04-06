import React from "react";
import AppLayout from "components/App.Layout";
import { Route ,Routes } from "react-router-dom";
import About from "./About";
import Home from "./Home";
import AccountsRoutes from "./accounts";
// import PostList from "components/PostList";
// import Post from "components/Post";

function Root(){
    return(
        <AppLayout>
            최상위 컴포넌트
            
          <Routes>
              <Route  path="/" element={<Home/>} />
              <Route  path="/about" element={<About />} />
              <Route path="/accounts/*" element={<AccountsRoutes />} />
          </Routes>
        </AppLayout>

    )
}
export default Root;
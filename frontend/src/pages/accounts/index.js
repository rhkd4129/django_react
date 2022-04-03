import React  from "react";
import Profile from "./profile";
import Login from "./Login";
import { Route,Routes } from "react-router-dom";

function Router( { match } ){
    // const { id } = useParams();
    return(
        <>
           
            <Routes>
                <Route path={match.url+"/profile"} element={<Profile />} />
                
                <Route path="/login" element={<Login />} />
                {/* <Route path="/signup" element={<Signup />} /> */}
            </Routes>
        </>
    )
}
export default Router;
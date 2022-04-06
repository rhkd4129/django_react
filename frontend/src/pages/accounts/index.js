import React  from "react";
import Profile from "./profile";
import Login from "./Login";
import { Route,Routes } from "react-router-dom";

function AccountsRoutes({match}){
    // const { id } = useParams();
    return(
        <>
           accounts/index
            <Routes>
                <Route path="/profile" element={<Profile />} />
                <Route path="/login" element={<Login />} />
                {/* <Route path="/signup" element={<Signup />} /> */}
            </Routes>
        </>
    )
}
export default AccountsRoutes;
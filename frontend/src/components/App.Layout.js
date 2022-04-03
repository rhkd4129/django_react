import React from "react";
import AppHeaders from "./AppHeaders";
import AppFooter from "./App.Footer";


function AppLayout({children}){
  
    return(
        <>
            <AppHeaders />
            {children}
            <AppFooter />
        
        </>
    );

}

export default AppLayout;
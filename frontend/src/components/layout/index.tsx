import LeftMenu from "./leftMenu.tsx";
import {Outlet} from "react-router-dom";
import "./index.css";

function Index() {
    return (
        <div className="layoutContainer">
            <LeftMenu/>
            <div className='contentContainer'>
                <div className="mainContent">
                    <Outlet/>
                </div>
            </div>
        </div>
    );
}

export default Index;

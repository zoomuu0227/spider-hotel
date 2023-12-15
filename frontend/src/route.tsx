import { ReactNode } from "react";
import Home from "./pages/home/index";
import Tujia from "./pages/tools/tujia.tsx";
import { BugOutlined, SendOutlined } from "@ant-design/icons";

export type MenuItemType = {
  path: string;
  Component: (() => ReactNode)  | null;
  title: string;
  hide?: boolean;
  icon?: ReactNode;
  children: MenuItemType[];
};
const routes: MenuItemType[] = [
  {
    path: "/",
    Component: Home,
    title: "首页",
    children: [],
    icon: <SendOutlined />,
  },
  {
    path: "/tools",
    Component: null,
    title: "爬虫",
    icon: <BugOutlined />,
    children: [
      {
        path: "tujia",
        title: "途家",
        Component: Tujia,
        children: [],
      },
    ],
  },
];
export default routes;

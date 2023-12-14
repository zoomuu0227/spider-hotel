import { ReactNode } from "react";
import Home from "./pages/home/index";
import { BugOutlined, SendOutlined } from "@ant-design/icons";

export type MenuItemType = {
  path: string;
  Component: (() => ReactNode) | string | null;
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
        Component: "/tools/tujia",
        children: [],
      },
    ],
  },
];
export default routes;

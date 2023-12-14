import React, { useEffect, useState } from "react";
import { MenuFoldOutlined, MenuUnfoldOutlined } from "@ant-design/icons";
import type { MenuProps } from "antd";
import { Button, Menu } from "antd";
import routes, { MenuItemType } from "../../route.tsx";
import { useLocation, useNavigate } from "react-router-dom";
import logo from "../../assets/logo.jpg";

type MenuItem = Required<MenuProps>["items"][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
  type?: "group",
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
    type,
  } as MenuItem;
}

const setMenuItem = (
  menus: MenuItemType[],
  father?: MenuItemType,
): MenuItem[] => {
  return menus
    .filter((item) => !item.hide)
    .map((item) => {
      return getItem(
        item.title,
        father ? father.path + "/" + item.path : item.path,
        item.icon,
        item.children.length ? setMenuItem(item.children, item) : undefined,
      );
    });
};

const App: React.FC = () => {
  const navigate = useNavigate();
  const pathname = useLocation().pathname;
  const pathArr = pathname.split("/");
  const parentPath = pathArr.slice(0, 2).join("/");
  const [items, setItems] = useState<MenuItem[]>([]);
  const [collapsed, setCollapsed] = useState(false);

  const [defaultKeys, setDefaultKeys] = useState<string[]>([]);
  const [defaultSelect, setDefaultSelect] = useState<string[]>([]);
  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };
  useEffect(() => {
    setItems(setMenuItem(routes));
    setDefaultSelect([pathname]);
    setDefaultKeys([parentPath]);
  }, []);

  return (
    <div
      className="leftMenuContainer"
      style={{
        width: !collapsed ? "256px" : "80px",
      }}
    >
      <div className="leftMenuTop">
        <img src={logo} alt="logo" className="logo" />
      </div>
      <div className="leftMenuBottom">
        <Button type="primary" onClick={toggleCollapsed} size="large">
          {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        </Button>
      </div>
      {defaultSelect.length && (
        <Menu
          defaultOpenKeys={defaultKeys}
          defaultSelectedKeys={defaultSelect}
          mode="inline"
          theme="dark"
          inlineCollapsed={collapsed}
          items={items}
          onSelect={(item) => {
            navigate(item.key);
          }}
        />
      )}
    </div>
  );
};

export default App;

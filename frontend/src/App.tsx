import { ConfigProvider, theme } from "antd";
import { Suspense } from "react";
import "./App.css";
import routes from "./route.tsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./components/layout";

function App() {
  return (
    <ConfigProvider
      theme={{
        algorithm: theme.darkAlgorithm,
        token: {
          // Seed Token，影响范围大
          colorPrimary: "rgb(125, 76, 219)",
        },
      }}
    >
      <BrowserRouter>
        <Suspense>
          <Routes>
            <Route Component={Layout}>
              {routes.map((f) => {
                return f.children.length > 0 ? (
                  <Route path={f.path} key={f.title} Component={f.Component}>
                    {f.children.length > 0 &&
                      f.children.map((c) => (
                        <Route
                          key={c.title}
                          path={c.path}
                          Component={c.Component}
                        />
                      ))}
                  </Route>
                ) : (
                  <Route path={f.path} Component={f.Component} key={f.title} />
                );
              })}
            </Route>
          </Routes>
        </Suspense>
      </BrowserRouter>
    </ConfigProvider>
  );
}

export default App;

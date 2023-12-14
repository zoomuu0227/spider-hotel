import { ConfigProvider, theme } from "antd";
import { lazy, Suspense } from "react";
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
                  <Route
                    path={f.path}
                    key={f.title}
                    Component={
                      typeof f.Component === "string"
                        ? lazy(() => import("./pages" + f.Component))
                        : f.Component
                    }
                  >
                    {f.children.length > 0 &&
                      f.children.map((c) => (
                        <Route
                          key={c.title}
                          path={c.path}
                          Component={lazy(
                            () => import("./pages" + c.Component),
                          )}
                        />
                      ))}
                  </Route>
                ) : (
                  <Route
                    path={f.path}
                    Component={
                      typeof f.Component === "string"
                        ? lazy(() => import("./pages" + f.Component))
                        : f.Component
                    }
                  />
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

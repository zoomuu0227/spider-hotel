import { Input, Button, Space, message, Table, Image, Modal, Spin } from "antd";
import type { ColumnsType } from "antd/es/table";
import { useState } from "react";
import citys from "../../config/city.ts";
import * as XLSX from "xlsx";

interface DataType {
  name: string;
  around: string;
  link: string;
  imgs: string[];
  address: string;
  videoUrl: string;
}

function getCityIdByName(name: string): string {
  let cityId = "";
  for (const item of citys) {
    for (const city of item.cities) {
      if (city.cityName === name) {
        cityId = city.cityId.toString();
        break;
      }
    }
  }
  return cityId;
}

function Index() {
  const [messageApi, contextHolder] = message.useMessage();
  const [city, setCity] = useState("");
  const [area, setArea] = useState("");
  const [data, setData] = useState<DataType[]>();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [source, setSource] = useState("");
  const [spinning, setSpinning] = useState<boolean>(false);
  const [selectDatas, setSelectDatas] = useState<DataType[]>([]);

  const columns: ColumnsType<DataType> = [
    {
      title: "酒店名称",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "链接",
      dataIndex: "link",
      key: "link",
      render: (_, { link }) => {
        return (
          <a href={link} target="_blank">
            {link}
          </a>
        );
      },
    },
    {
      title: "地址",
      dataIndex: "address",
      key: "address",
    },
    {
      title: "周边",
      dataIndex: "around",
      key: "around",
    },
    {
      title: "图片",
      dataIndex: "imgs",
      key: "imgs",
      render: (_, { imgs }) => {
        return imgs.length > 0 ? (
          <Image.PreviewGroup>
            {imgs.map((src, index) => (
              <Image width={20} src={src} key={index} />
            ))}
          </Image.PreviewGroup>
        ) : (
          <></>
        );
      },
    },
    {
      title: "视频",
      dataIndex: "videoUrl",
      key: "videoUrl",
      render: (_, { videoUrl }) => {
        return videoUrl !== "" ? (
          <Button
            type="link"
            onClick={() => {
              setSource(videoUrl);
              setIsModalOpen(true);
            }}
          >
            观看
          </Button>
        ) : (
          <></>
        );
      },
    },
  ];
  const submit = () => {
    const cityId = getCityIdByName(city);
    if (cityId === "") {
      messageApi.error("城市名不正确");
      return;
    }
     // http://192.168.3.174:5174/

    const url = `http://localhost:8088/crawl?id=${cityId}&name=${city}&area=${area}`;
    setSpinning(true);
    fetch(url)
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        if (res.code === 200) {
          setData(res.data);
        } else {
          messageApi.error(res.msg);
        }
        setSpinning(false);
      });
  };
  const exportData = () => {
    if (selectDatas.length === 0) {
      messageApi.error("请选择导出数据");
      return;
    }
    const fileName = city + area + ".xlsx";
    const worksheet = XLSX.utils.json_to_sheet(selectDatas);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, worksheet, "Sheet1");
    XLSX.writeFile(wb, fileName);
  };
  return (
    <Spin spinning={spinning}>
      <Space>
        {contextHolder}
        <Input
          placeholder="请输入城市名称"
          value={city}
          onChange={(e) => {
            setCity(e.target.value);
          }}
        />
        <Input
          placeholder="请输入景点名称"
          value={area}
          onChange={(e) => {
            setArea(e.target.value);
          }}
        />
        <Button type="primary" onClick={submit}>
          获取
        </Button>
      </Space>
      <div
        style={{
          padding: "10px 0",
        }}
      >
        <Button type="dashed" onClick={exportData}>
          导出
        </Button>
      </div>
      <Table
        rowKey="link"
        columns={columns}
        pagination={{
          pageSize: 100,
        }}
        dataSource={data}
        size="small"
        rowSelection={{
          type: "checkbox",
          onChange: (_, selectedRows: DataType[]) => {
            setSelectDatas(selectedRows);
          },
        }}
      />
      <Modal
        title="视频"
        open={isModalOpen}
        footer={null}
        width={850}
        onCancel={() => {
          setIsModalOpen(false);
        }}
      >
        <video controls width="800" key={source}>
          <source src={source} type="video/webm" />
          <source src={source} type="video/mp4" />
        </video>
      </Modal>
    </Spin>
  );
}

export default Index;

import React, { Fragment } from "react";
import Form from "./Form";
import Coffees from "./Coffees";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Coffees />
    </Fragment>
  );
}

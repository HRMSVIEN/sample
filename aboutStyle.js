import { Typography } from "@mui/material";

export const AboutTypography = (props) => (
  <Typography
    style={{
      fontWeight: "bold",
      fontSize: "2.2rem",
      background: "linear-gradient(90deg, #d500f9 30%, #ff4081 90%)", // purple to pink
      WebkitBackgroundClip: "text",
      WebkitTextFillColor: "transparent",
      marginBottom: "1.2rem",
      letterSpacing: "1px",
    }}
    {...props}
  >
    {props.children}
  </Typography>
);

export const BodyTypography = (props) => (
  <Typography
    style={{
      fontSize: "1.15rem",
      lineHeight: 1.8,
      color: "#ad1457", // deep pink
      marginBottom: "1rem",
    }}
    {...props}
  >
    {props.children}
  </Typography>
);

export const StoryTypography = (props) => (
  <Typography
    style={{
      color: "#8e24aa", // purple
      fontWeight: "bold",
      fontSize: "1.4rem",
      marginTop: "2.5rem",
      marginBottom: "0.7rem",
      letterSpacing: "0.5px",
    }}
    {...props}
  >
    {props.children}
  </Typography>
);

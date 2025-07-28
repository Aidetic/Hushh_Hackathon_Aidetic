"use client";

import { useState } from "react";
import {
  Card,
  CardContent,
  Typography,
  Collapse,
  Box,
  Chip,
  IconButton,
} from "@mui/material";
import { ExpandMore, ExpandLess } from "@mui/icons-material";
import iphoneImg from "../assets/apple-iphone.png";

const ResultCard = ({
  shop_name,
  product,
  discount,
  personalized_offer,
  offer_price,
  true_price,
}) => {
  const [expanded, setExpanded] = useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card
      sx={{
        mb: 2,
        width: "100%", // full width
        borderRadius: 6,
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
        transition: "transform 0.2s ease-in-out",
        "&:hover": {
          transform: "translateY(-2px)",
          boxShadow: "0 4px 16px rgba(0,0,0,0.15)",
        },
      }}
    >
      <CardContent>
        {/* Shop name */}
        <Typography
          variant="h6"
          component="h3"
          color="primary"
          sx={{ fontWeight: "bold", mb: 1, fontSize: "1.5rem" }}
        >
          {shop_name}
        </Typography>

        {/* Main content layout */}
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            gap: 2,
            flexWrap: "wrap",
          }}
        >
          {/* Left image */}
          <Box
            component="img"
            src={iphoneImg}
            alt="image"
            sx={{
              minWidth: 80,
              height: 80,
              objectFit: "cover",
              borderRadius: 1,
            }}
          />

          {/* Product name */}
          <Box sx={{ flex: 1, minWidth: 200 }}>
            <Typography
              variant="body1"
              sx={{ fontWeight: "bold", fontSize: "1.5rem", color: "primary" }}
            >
              {product}
            </Typography>
          </Box>

          {/* Right section */}
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              alignItems: "flex-end",
              minWidth: 120,
            }}
          >
            <Typography
              variant="body2"
              sx={{ fontWeight: "bold", color: "primary", fontSize: "1.5rem" }}
            >
              Offer Price: {offer_price}
            </Typography>
            <Typography
              variant="body2"
              sx={{
                color: "#929292",
                textDecoration: "line-through",
                mt: 0.5,
                fontSize: "1.4rem",
              }}
            >
              True Price: {true_price}
            </Typography>
            <Chip
              label={`${discount}% OFF`}
              color="secondary"
              sx={{ fontWeight: "bold", mt: 1, fontSize: "1rem" }}
            />
          </Box>
        </Box>

        <IconButton
          onClick={handleExpandClick}
          sx={{ mt: 2 }}
          aria-label={expanded ? "Hide Offer" : "Show Offer"}
        >
          {expanded ? <ExpandLess /> : <ExpandMore />}
        </IconButton>

        <Collapse in={expanded} timeout="auto" unmountOnExit>
          <Box
            sx={{
              mt: 1,
              p: 2,
              backgroundColor: "#fff",
              borderRadius: 1,
              border: "1px solid #000",
            }}
          >
            <Typography
              variant="body2"
              sx={{
                fontStyle: "italic",
                fontWeight: "bold",
                color: "primary",
                fontSize: "1.3rem",
              }}
            >
              {personalized_offer}
            </Typography>
          </Box>
        </Collapse>
      </CardContent>
    </Card>
  );
};

export default ResultCard;

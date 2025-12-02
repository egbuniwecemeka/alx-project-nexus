document.addEventListener("DOMContentLoaded", function () {

    const payBtn = document.getElementById("pay-btn");

    if (payBtn) {
        payBtn.addEventListener("click", function () {
            fetch("/create-checkout-session/", {method: "POST"})
                .then(res => res.json())
                .then(data => {
                    const stripe = Stripe(stripe_public_key);
                    return stripe.redirectToCheckout({
                        sessionId: data.id
                    });
                })
                .catch(err => console.error("Stripe error:", err)
            );
        });
    }

});

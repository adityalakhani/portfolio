document.addEventListener("DOMContentLoaded", function () {
    document.body.addEventListener("click", function (e) {
        const button = e.target.closest(".copy-button");
        if (button) {
            const pre = button.closest(".code-snippet-pre");
            if (!pre) return;

            const codeBlock = pre.querySelector("code");
            if (!codeBlock) return;

            const text = codeBlock.innerText;
            navigator.clipboard.writeText(text).catch(err => {
                console.error("Failed to copy text: ", err);
            });
        }
    });
});

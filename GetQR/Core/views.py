
from rest_framework.decorators import api_view
from rest_framework.response import Response
import qrcode
import io
import base64
# Create your views here.

@api_view(["GET","POST"])
def makeqr(request):
    if request.method == 'POST':
        
        drsum = 2.5 * int(request.data.get("mil")) * 2 -20

        request.data["DRSum"] = drsum
        request.data["paymentID"] = drsum

        img = qrcode.make(request.data)
        image = io.BytesIO()
        img.save(stream=image)
        base64_image = base64.b64encode(image.getvalue()).decode()

        main_code = 'data:image/png;utf8;base64,' + base64_image
        
        return Response({"qr":main_code})

    return Response({"message":"please pass the needed informations"})


{
    "Member Profile":"John T Henry",
    "Member_ID":"22344",
    "DriverID":"840JOG",
    "Payment_Amt":"15.65",
    "BankIntID":"Bofa",
    "DebtCD":"9998",
    "Debtexp":"0924",
    "DebtCVV":"778",
    "TextAlertNFC":"626.991.1174",
    "NonMID":"626.991.1174",
    "mil":"10"
}